# datadog-exim
 
{{{
cd /etc/datadog-agent/conf.d
wget 

cd /etc/datadog-agent/checks.d
wget 

# Add the dd-agent user to the exim group so that it can run the command 'exim -bpc' to find out the queue length
usermod -a -G exim dd-agent

}}}

Run this to test the new check:
datadog-agent check exim

If there is an error run this to get detail and investigate:
datadog-agent check exim -l debug | less

If it works run this to restart datadog-agent:
initctl restart datadog-agent

In the datadog GUI go to metric explorer and search for exim. It should show up with the current number of items 
in the exim message queue


