$folder = Read-Host "Enter folder name"
if (-not (Test-Path $folder -PathType Container)) {
    Write-Host "Folder does not exist"
    exit 1
}
Set-Location $folder
$max = 0
Get-ChildItem -Filter "day*.mac" | ForEach-Object {
    $name = $_.BaseName
    $num = $name -replace "day", ""
    if ([int]$num -gt $max) { $max = [int]$num }
}
$next = $max + 1
Write-Host "This will be the day $next"
New-Item -ItemType File -Name "day$next.mac" -Value ""
Write-Host "Created day$next.mac in $folder"