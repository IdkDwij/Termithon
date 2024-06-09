# Neofetch-like System Info Script for PowerShell

# Function to get OS info
function Get-OSInfo {
    $os = Get-CimInstance Win32_OperatingSystem
    [PSCustomObject]@{
        "OS" = $os.Caption
        "Version" = $os.Version
        "Build" = $os.BuildNumber
    }
}

# Function to get system info
function Get-SystemInfo {
    $sys = Get-CimInstance Win32_ComputerSystem
    [PSCustomObject]@{
        "Manufacturer" = $sys.Manufacturer
        "Model" = $sys.Model
    }
}

# Function to get CPU info
function Get-CPUInfo {
    $cpu = Get-CimInstance Win32_Processor
    [PSCustomObject]@{
        "Processor" = $cpu.Name
    }
}

# Function to get Memory info
function Get-MemoryInfo {
    $mem = Get-CimInstance Win32_PhysicalMemory
    $totalMem = ($mem | Measure-Object -Property Capacity -Sum).Sum
    [PSCustomObject]@{
        "Memory (GB)" = [math]::Round($totalMem / 1GB, 2)
    }
}
function Get-DiskInfo {
    $disk = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"
    $diskInfo = @()
    foreach ($d in $disk) {
        $diskInfo += [PSCustomObject]@{
            "Drive" = $d.DeviceID
            "File System" = $d.FileSystem
            "Free Space (GB)" = [math]::Round($d.FreeSpace / 1GB, 2)
            "Total Space (GB)" = [math]::Round($d.Size / 1GB, 2)
        }
    }
    return $diskInfo
}

function Get-GPUInfo {
    $gpu = Get-CimInstance Win32_VideoController
    $gpuInfo = @()
    foreach ($g in $gpu) {
        $gpuInfo += [PSCustomObject]@{
            "GPU" = $g.Name
            "VRAM" = [math]::Round($g.AdapterRAM / 1MB, 2)
        }
    }
    return $gpuInfo
}

# Function to display info
function Display-Info {
    $asciiLogo = @"


 lllllllllllllll   lllllllllllllll
  lllllllllllllll   lllllllllllllll
   lllllllllllllll   lllllllllllllll
    lllllllllllllll   lllllllllllllll
     lllllllllllllll   lllllllllllllll
      lllllllllllllll   lllllllllllllll

        lllllllllllllll   lllllllllllllll
         lllllllllllllll   lllllllllllllll
          lllllllllllllll   lllllllllllllll
           lllllllllllllll   lllllllllllllll
            lllllllllllllll   lllllllllllllll
             lllllllllllllll   lllllllllllllll



"@


    Write-Host $asciiLogo -ForegroundColor Blue -NoNewline

    $osInfo = Get-OSInfo
    $sysInfo = Get-SystemInfo
    $cpuInfo = Get-CPUInfo
    $memInfo = Get-MemoryInfo
    $diskInfo = Get-DiskInfo
    $gpuInfo = Get-GPUInfo

    Write-Host "OS:" -ForegroundColor Blue -NoNewline; Write-Host " $($osInfo.OS) $($osInfo.Version) (Build $($osInfo.Build))"
    Write-Host "Host:" -ForegroundColor Blue -NoNewline; Write-Host " $($sysInfo.Manufacturer) $($sysInfo.Model)"
    Write-Host "CPU:" -ForegroundColor Blue -NoNewline; Write-Host " $($cpuInfo.Processor)"
    Write-Host "Memory:" -ForegroundColor Blue -NoNewline; Write-Host " $($memInfo.'Memory (GB)') GB"
    Write-Host "Disk Info: " -ForegroundColor Blue -NoNewLine; Write-Host 
    foreach ($disk in $diskInfo) {
        $disk.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }
        Write-Host ""
    }
    Write-Host "GPU: " -ForegroundColor Blue -NoNewLine; Write-Host 
    foreach ($gpu in $gpuInfo) {
        $gpu.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }
        Write-Host ""
    }
}

# Run the display function
Display-Info
