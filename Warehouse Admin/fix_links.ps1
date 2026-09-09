$files = Get-ChildItem -Path "c:\Users\DK\Desktop\Logistics\Logistics-Admin" -Recurse -Filter "*.html"
foreach ($f in $files) {
    $text = [System.IO.File]::ReadAllText($f.FullName)
    $changed = $false
    if ($text.Contains('href="../Audit-Logs/index.html"')) {
        $text = $text.Replace('href="../Audit-Logs/index.html"', 'href="../../Admin/Audit-Logs/index.html"')
        $changed = $true
    }
    if ($text.Contains('href="../Role-Permission/index.html"')) {
        $text = $text.Replace('href="../Role-Permission/index.html"', 'href="../../Admin/Role-Permission/index.html"')
        $changed = $true
    }
    if ($changed) {
        [System.IO.File]::WriteAllText($f.FullName, $text)
        Write-Output "Fixed: $($f.FullName)"
    }
}
