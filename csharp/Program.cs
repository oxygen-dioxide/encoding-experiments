using System.Text;

Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);
var a=Encoding.GetEncoding(0);
Console.WriteLine(a.EncodingName);
Console.WriteLine(a.WebName);
Console.WriteLine(a.CodePage);
