package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
)

type order struct {
	ID     string  `json:"id"`
	Item   string  `json:"item"`
	Amount float64 `json:"amount"`
}

var orders = []order{
	{ID: "1", Item: "widget", Amount: 9.99},
	{ID: "2", Item: "gadget", Amount: 24.50},
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /healthz", func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(http.StatusOK)
	})
	mux.HandleFunc("GET /orders", func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(orders)
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	log.Printf("orders-api listening on :%s", port)
	log.Fatal(http.ListenAndServe(":"+port, mux))
}
