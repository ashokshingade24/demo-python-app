import logging
import time
import random

# Configure logging to standard output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("LokiDemoApp")

messages = ["User logged in", "Order processed", "Payment failed", "Cache refresh started"]

if __name__ == "__main__":
    while True:
        msg = random.choice(messages)
        level = random.choice(["INFO", "WARNING", "ERROR"])
        
        if level == "ERROR":
            logger.error(f"Something went wrong: {msg}")
        elif level == "WARNING":
            logger.warning(f"Check this out: {msg}")
        else:
            logger.info(msg)
            
        time.sleep(2)
