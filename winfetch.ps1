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
        "System Type" = $sys.SystemType
    }
}

# Function to get CPU info
function Get-CPUInfo {
    $cpu = Get-CimInstance Win32_Processor
    [PSCustomObject]@{
        "Processor" = $cpu.Name
        "Cores" = $cpu.NumberOfCores
        "Threads" = $cpu.NumberOfLogicalProcessors
    }
}

# Function to get GPU info
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

# Function to get Memory info
function Get-MemoryInfo {
    $mem = Get-CimInstance Win32_PhysicalMemory
    $totalMem = ($mem | Measure-Object -Property Capacity -Sum).Sum
    [PSCustomObject]@{
        "Total Memory" = [math]::Round($totalMem / 1GB, 2)
    }
}

# Function to get Disk info
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

# Function to display info
function Display-Info {
    Write-Host "Neofetch for PowerShell" -ForegroundColor Cyan
    Write-Host "======================="

    $osInfo = Get-OSInfo
    Write-Host "`nOS Information:`n-----------------"
    $osInfo.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }

    $sysInfo = Get-SystemInfo
    Write-Host "`nSystem Information:`n----------------------"
    $sysInfo.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }

    $cpuInfo = Get-CPUInfo
    Write-Host "`nCPU Information:`n-----------------"
    $cpuInfo.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }

    $gpuInfo = Get-GPUInfo
    Write-Host "`nGPU Information:`n-----------------"
    foreach ($gpu in $gpuInfo) {
        $gpu.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }
        Write-Host ""
    }

    $memInfo = Get-MemoryInfo
    Write-Host "`nMemory Information:`n-------------------"
    $memInfo.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }

    $diskInfo = Get-DiskInfo
    Write-Host "`nDisk Information:`n-------------------"
    foreach ($disk in $diskInfo) {
        $disk.PSObject.Properties | ForEach-Object { Write-Host ($_.Name + ": " + $_.Value) }
        Write-Host ""
    }
}

# Run the display function
Display-Info
