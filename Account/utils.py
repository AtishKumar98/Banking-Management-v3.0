import random
import uuid ,base64 

def generate_code():
    
    code = str(uuid.uuid4())[:12]
    return code



def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))