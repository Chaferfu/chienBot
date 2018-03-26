repliques = []
repliques.append("Waf!")
repliques.append("Wuf!")
repliques.append("Wef!")
repliques.append("Wif!")
repliques.append("Wof!")
repliques.append("Wouf!")
repliques.append("Wigrecf!")

if __name__=="__main__":
	mode = "-1"
	while ((int(mode) < 0) or (int(mode) > 3)): 
		mode = input();
	{
		0 : "Mode 0",
		1 : "Mode 1",
		2 : "Mode 2",
		3 : "Mode 3"
	}[int(mode)]
