package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){
	file, _ := os.Open("classificationLibLinear.txt")
	sc := bufio.NewScanner(file)

	
	currentClassification := make(map[string]int)
	var countRight int
	var countTot int
	
	var precLanguage string
	for i:=1; sc.Scan(); i++{
		line := strings.Fields(sc.Text())
		if i==1{
			precLanguage = line[1]
		}
		currentClassification[line[2]]++
		if i%300 == 0 || precLanguage != line[1]{
			maxLab := ""
			for k, v := range currentClassification{
				if v > currentClassification[maxLab]{
					maxLab = k
				}
			}
			fmt.Printf("The label should be %s, it was %s\n", line[1], maxLab)

			if line[1] == maxLab{
				countRight++
			}
			countTot++

			currentClassification = make(map[string]int)
			precLanguage = line[1]
		}
	}
	fmt.Printf("%d/%d are correct\n",countRight, countTot)

}