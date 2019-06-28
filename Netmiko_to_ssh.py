import Netmiko

def ssh(device_type, ipaddress):
    """
    This function is used for performing ssh to linux devices
    :param device_type: The device for which you want to perform ssh login.
    :param ipaddress: IP address of the device.
    :return: connection | None
    """
    try:
        connection = netmiko.ConnectHandler(device_type='cisco_ios', host=ipaddress, username=DEVICE_LOGIN_USERNAME,
                                    password=DEVICE_LOGIN_PASSWORD)
        logging.info(f'Now we have logging into {device_type} {ipaddress}')
    except netmiko.ssh_exception.SSHException as ssh_err:
        logging.error("Issue observed with ssh to IP: %s - %s" % (ipaddress, str(ssh_err)))
        return None
    except netmiko.NetMikoAuthenticationException as auth_err:
        logging.error("%s is not authorized to access device with IP: %s"
                      " - %s" % (os.environ["USER"], ipaddress, str(auth_err)))
        return None
    except netmiko.NetMikoTimeoutException as timeout_err:
        logging.error("Device connection timeout - %s" % str(timeout_err))
        return None
    else:
        return connection
        
connection = ssh('xyz device', '10.11.12.13')
if not connection:
  pass
else:
  '''Perform required action after logging into the device'''
  
