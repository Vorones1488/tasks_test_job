import asyncio

import aio_pika

from src.config import setting, Settings
from src.utilit.message_broker.rabbitmq.worker import worker


#


async def make_amqp_consumer(setting: Settings):
    connection = await aio_pika.connect_robust(setting.url_amqp)
    channel = await connection.channel()
    queue = await channel.declare_queue(setting.RABBITMQ_QUEUE_TASK, durable=True)
    await queue.consume(worker.consume_task, no_ack=False)


# if __name__ == "__main__":
#     asyncio.run(main())
