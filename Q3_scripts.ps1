# One of the alternative to do the output 3, The other one is specify github path in docker-compose.yml

Write-Host "This script will pull the git repository for Q3 into
the current file path and run the docker-compose file."

$consent = Read-Host "Do you want to process (Y/n)"

if($consent -eq "Y") 
{
    Write-Host "Proceed to pull git repository."
}
else
{
    Write-Host "Exit"
    Exit
}

if (Test-Path -Path $PWD/tonson_exam/Q3)
{
    Write-Host "There is already existing git repository, proceed to run docker-compose"
}
else 
{
    git clone https://github.com/TonsonP/Docker_API.git $PWD\tonson_exam
    Write-Host "Download Q3 git repository"
}

docker-compose -f $PWD/tonson_exam/Q3/docker-compose.yml build
docker-compose -f $PWD/tonson_exam/Q3/docker-compose.yml up


