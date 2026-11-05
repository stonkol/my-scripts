on run {input, parameters}
    repeat with fileAlias in input
        set posixPath to POSIX path of fileAlias
        set fileType to do shell script "file -b -- " & quoted form of posixPath

        if fileType contains "PDF" or fileType contains "JPEG" or fileType contains "PNG" or fileType contains "ISO Media" then
            do shell script "exiftool -all= " & quoted form of posixPath
        else
            display dialog "Unsupported file type: " & fileType
        end if
    end repeat

    return input
end run
