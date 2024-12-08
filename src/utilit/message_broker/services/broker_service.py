# import json
#
#
#
#
#
#
#
#
# class BrockerService:
#     async def add_task_broker(self, message: dict) -> bool:
#         '''Queues a message'''
#         message_json = json.dumps(message)
#         if await rabbit_connection.send_message(message_json):
#              return True
#         return False
# broker_service = BrockerService()
