echo off

setlocal

start ssh-agent

set SSH_AUTH_SOCK=%TEMP%\ssh-agent.sock

echo %userprofile%

ssh-add ..\..\..\.ssh\github

endlocal