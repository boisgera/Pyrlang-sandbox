

#
import logging

from colors import color

from pyrlang.node import Node
from term import Atom

LOG = logging.getLogger(color("EXAMPLE1", fg='lime'))


async def example_main(node):
    fake_pid = node.register_new_process()

    # To be able to send to Erlang shell by name first give it a registered
    # name: `erlang:register(shell, self()).`
    # To see an incoming message in shell: `flush().`
    await node.send(sender=fake_pid,
                    receiver=(Atom("oddball@192.168.1.85"), Atom('target')),
                    message=Atom('hello'))
    LOG.info("example_main: Done")


def main():
    node = Node(node_name="py@192.168.1.85", cookie="banana")
    ev = node.get_loop()
    ev.create_task(example_main(node))
    node.run()


if __name__ == "__main__":
    main()
