Write-Host "This script will pull the git repository for Q3 if not existing yet,
and run the docker compose from the downloaded git repository"

$consent = Read-Host "Do you want to process (Y/n)"

if($consent -eq "Y") 
{
    Write-Host "Proceed to pull git repository"
}
else
{
    Write-Host "Exit"
    Exit
}
