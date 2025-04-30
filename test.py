import pexpect
#from pexpect import spawn
import sys
import os
from datetime import datetime

try:
    child = pexpect.spawn('ssh svc-net-ansible-cli@10.50.49.62')
    child.expect('password:')
    child.sendline('N!-}f9I$94nhuf6!Rh;Wy4qymH8Cy.')
    child.expect('# ')  # Assuming a bash prompt
    child.sendline('ping 10.50.49.62')
    child.expect('*[#$>].* ')
    print(child.before.decode())
    child.sendline('exit')
    child.expect(pexpect.EOF)

except pexpect.exceptions.ExceptionPexpect as e:
    print(f"Pexpect error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'child' in locals() and child.isalive():
        child.close()
