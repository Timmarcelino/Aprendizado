var objArgs = WScript.Arguments;
for (var i = 0; i < objArgs.Count(); i++)
{
    WScript.Echo(objArgs(i));
}