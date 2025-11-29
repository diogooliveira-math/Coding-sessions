# PowerShell script to free port 4096 by killing processes using it
$port = 4096
$netstat = netstat -ano | Select-String ":$port"
if ($netstat) {
    $procIds = $netstat | ForEach-Object {
        ($_ -split '\s+')[-1]
    } | Sort-Object -Unique
    foreach ($procId in $procIds) {
        try {
            Write-Host "Killing PID $procId..."
            taskkill /PID $procId /F | Out-Null
        } catch {
            Write-Host "Failed to kill PID $procId"
        }
    }
    Write-Host "Port $port is now free."
} else {
    Write-Host "No process is using port $port."
}