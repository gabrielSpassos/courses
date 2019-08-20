program	BasicPascal(output);

var
   result : integer;

procedure sayHello();
	begin
		writeln('Hello World!')
	end;
	
function returnInt(): integer;
	begin
		returnInt:= 10;
	end;
	
begin
	sayHello();
	result := returnInt();
    writeln(result)
end.