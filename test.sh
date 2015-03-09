#!/bin/bash

function retrieve { #this sets the global variable equationString to the equation in string form
	echo "Enter an equation in the form ax^2+bx+c: "
	read equationString
}

function getsign { #this increases the global variable position and returns an integer for sign
	sign=${equation:$position:1}
	let position=$position+1
	if [ "$sign" = "-" ]; then
		echo -1
	else
		echo 1
	fi
}

function parse { #uses global equation variable which is a string. sets global vars a, b, c, and position
	position=0
	a=$(getNum)
	position=($position+3)
	local bSign=$(getsign)
	b=$(getNum)
	b=(expr $b \* $bSign)
	position=($position+1)
	c=$(getNum)
}

function getNum { # returns by echo much like return statements
	local strNum=""
	if [ ${equation:$position:1} = 'x' ]; then
		echo 1
	else
		while [ ${equation:$position:1} != 'x']; do
			let strNum=(strNum+${equation:$position:1})
			let position=(position+1)
			if [ $position = ${#equation} ]; then
				break
			fi
		done
		echo $strNum
	fi
}

function simplify { # passed an argument, makes global var discriminant
	inside=$1
	number=$1
	discriminant=(1 'r' 1)
	if [ $inside = 0 ]; then
		let discriminant=(0 'r' 0)
	elif [ $inside < 0 ]; then
		let discriminant[1]='i'
		let inside=(expr $inside \* -1)
		let number=(expr $number \* -1)
	fi
	devisor=2
	out=$(simplifyHelper)
	discriminant[0]=$out
	discriminant[2]=$inside
}

function simplifyHelper { # recursively calls itself until it has tested 2 -> 50, echos answer
	if [ devisor -lt 50 ]; then
		let inside=$number
		echo 1
	else
		outside=1
		squared="$devisor**2"
		if [ $(expr $number % $squared) -eq 0 ]; then
			let outside=devisor
			let number=$(expr $number / $squared)
			echo $(expr outside \* simplifyHelper)
		else
			let devisor=devisor+1
			echo $(expr outside \* simplifyHelper)
}

function reduction { # uses global bTerm, discriminant, and denominator
	for i in 'seq $denominator 1 -1'; do
		if [ $(expr $bTerm % $i) -eq 0 && $(expr %discriminant[0] % $i) -eq 0 && $(expr $denominator % i) -eq 0 ]; then
			let bTerm=$(expr $bTerm / $i)
			let discriminant[0]=$(expr $discriminant[0] / $i)
			let denominator=$(expr $denominator / $i)
}

function stringify {
	local first="$bTerm"
	local second=$(discString)
	if [ $denominator -ne 1 ]; then
		local third="\n"
		for i in 'seq 1 ${#$("'
}

equation='a'
echo ${#equation}
position=0