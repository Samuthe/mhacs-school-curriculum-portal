package greetings

import (
	"errors"
	 "fmt"
	"math/rand"
	"time"
)

func Hello(name string) (string, error){
	if name == "" {
		return "", errors.New("empty name")
}
	message:=fmt.Sprintf(randomFormat(), name)
	return message, nil
}

func Hellos(names []string) (map[string]string, error){
	messages := make(map[string]string)
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}
		messages[name] = message
	}
	return messages, nil
}

func randomFormat() string {
	rand.Seed(time.Now().UnixNano())

	formats := []string {
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
		"This is soo cheesy %v. What do you think?",
		"Do you love coding %v?",
}

return formats[rand.Intn(len(formats))]
}
