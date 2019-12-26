import concurrent.futures
import logging
from queue import Queue
from typing import Iterable, Sequence

from util import queue_to_list, Program, Computer, ComputerSignals

LOG = logging.getLogger(__name__)


def calc_amp(amp_program: Program, phase_config: Iterable[int]):
    input_ = 0
    for phase in phase_config:
        inq = Queue()
        inq.put(phase)
        inq.put(input_)
        outq = Queue()
        amplifier = Computer(amp_program,input_queue=inq,output_queue=outq)
        amplifier.run_until_stop()
        amp_output = [i for i in queue_to_list(outq) if not isinstance(i,ComputerSignals)]
        assert len(amp_output) == 1
        input_ = amp_output[-1]
    return amp_output[-1]


def run_computer_on_queues(program: Program, in_q: Queue, out_q: Queue):
    c = Computer(program, input_queue=in_q, output_queue=out_q)
    logging.debug("Starting execution of some program.")
    c.run_until_stop()
    logging.debug("The program has stopped.")


def calc_amp_with_feedback(amp_program: Program, phase_config: Sequence[int]):
    input_and_feedback_queue = Queue()
    input_and_feedback_queue.put(phase_config[0])
    input_and_feedback_queue.put(0)
    a_to_b_queue = Queue()
    a_to_b_queue.put(phase_config[1])
    b_to_c_queue = Queue()
    b_to_c_queue.put(phase_config[2])
    c_to_d_queue = Queue()
    c_to_d_queue.put(phase_config[3])
    d_to_e_queue = Queue()
    d_to_e_queue.put(phase_config[4])

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.submit(run_computer_on_queues, amp_program, input_and_feedback_queue, a_to_b_queue)
        executor.submit(run_computer_on_queues, amp_program, a_to_b_queue, b_to_c_queue)
        executor.submit(run_computer_on_queues, amp_program, b_to_c_queue, c_to_d_queue)
        executor.submit(run_computer_on_queues, amp_program, c_to_d_queue, d_to_e_queue)
        executor.submit(run_computer_on_queues, amp_program, d_to_e_queue, input_and_feedback_queue)

    outs = queue_to_list(input_and_feedback_queue)

    return outs[-2]
