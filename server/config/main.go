package config

import (
	"fmt"
	"github.com/micro/go-micro/v2/config"
	"github.com/micro/go-micro/v2/config/source/file"
)

// define our own host type
type EmailConfig struct {
	ADDR     string `json:"addr"`
	HOST     string `json:"host"`
	USER     string `json:"user"`
	NAME     string `json:"name"`
	PASSWORD string `json:"password"`
}

func GetEmailCnfig() EmailConfig {
	var emailconfig EmailConfig
	if err := config.Load(file.NewSource(
		file.WithPath("./server/config/config.json"),
	)); err != nil {
		fmt.Println("err", err)
		return emailconfig
	}

	if err := config.Get("email").Scan(&emailconfig); err != nil {
		fmt.Println("err", err)
		return emailconfig
	}
	return emailconfig
}

