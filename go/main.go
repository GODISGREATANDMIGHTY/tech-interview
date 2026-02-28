package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	wg := sync.WaitGroup{}
	ch1 := make(chan int)
	ch2 := make(chan int)

	wg.Add(2)
	go func() {
		defer wg.Done()

		for {
			<-ch1
			fmt.Println("A")
			ch2 <- 0

			time.Sleep(time.Second * 1)
		}
	}()

	go func() {
		defer wg.Done()

		for {
			<-ch2
			fmt.Println("B")
			ch1 <- 0

			time.Sleep(time.Second * 1)
		}

	}()

	fmt.Println("main function exited")
	ch1 <- 0
	wg.Wait()
}
