#DEVICE_LOGIN_PASSWORD is the variable which stores the user password.

def cli_executer(connection, command, device_type):
    """
    This function is to execute commands on load balancer.
    :param connection: Conenction is the ssh object created from ssh function.
    :param command: Command we want to execute on linux device.
    :return: This function returns the output of command along with the ssh connection object.
    """
    
    if command != DEVICE_LOGIN_PASSWORD:
        logging.info(f'Currently executing : {command}')
    
    '''While loop is executed until we find the device prompt after receiving command output, '''
    ''''#' is used to find the device prompt here along with send_command_expect().'''
    if device_type == 'lb':
        output = ''
        j = 1
        while not output and j <10:
            output = connection.send_command_expect(command, expect_string=r'#')
            time.sleep(1)
            j += 1
    
    '''send_command_timing() is used to send command and receive output but sometimes it fails to wait till it receives device prompt.'''
    elif device_type == 'fw':
        output = connection.send_command_timing(command)
        
    elif device_type == 'router' and 'traceroute' in command:
        logging.info('Please wait for 30 seconds while Script is performing Traceroute test')
        connection.write_channel(command + '\n')
        i = 0
        while i < 30:
            i += 1
            print(f"{i} sec.")
            time.sleep(1)

        logging.info("Executing \"Ctrl + Shift + 6\" to abort traceroute if it's not over within 30 seconds")
        ctrl_shift_6 = chr(30)
        connection.write_channel(ctrl_shift_6)

        output = connection.read_channel()
    else:
        logging.error('Please enter the device type as lb or fw')
    print(output)
    return output, connection
    
    
access_list_output = cli_executer(connection, 'show access-list', 'firewall')
