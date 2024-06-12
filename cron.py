# from apscheduler.schedulers.background import BackgroundScheduler
# from new import job 
# from apscheduler.schedulers.blocking import BlockingScheduler
# import time
# from datetime import datetime
# import pycron


# if __name__ == '__main__':
#     while True:
#         if pycron.is_now("*/1 * * * * *"):  # Check if it's time to run the job
#             job()
#         # Sleep for a short interval to avoid using too much CPU
#         time.sleep(0.1)

# # @pycron.cron("*/1 * * * * *", job)
# # async def test(timestamp: datetime):
# #     print(f"test cron job running at {timestamp}")

# # if __name__ == '__main__':
# #     pycron.start()
# #     print("Scheduler started. Press Ctrl+C to exit.")

# # if __name__ == "__main__":
# #     scheduler = BlockingScheduler()
# #     # Schedule the job to run every minute
# #     scheduler.add_job(job, 'interval', minutes=1)
# #     print("Scheduler started. Press Ctrl+C to exit.")
# #     try:
# #         scheduler.start()
# #     except (KeyboardInterrupt, SystemExit):
# #         pass