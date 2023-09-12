versao = wscript.version
maiorversao = ScriptEngineMajorVersion()
menorversao = ScriptEngineMinorVersion()

if versao >= "5.1" then
	msg = "Wsh está atualizado ( " & maiorversao & "." & menorversao & ")" & vbcrlf
else
	msg = "Wsh não está atualizado, a versão mínima recomendável é 5.1 e a sua é " & maiorversao & "." & menorversao & vbcrlf
end if

wscript.echo msg