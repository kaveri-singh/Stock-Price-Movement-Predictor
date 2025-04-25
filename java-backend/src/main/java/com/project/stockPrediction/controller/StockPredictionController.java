package com.project.stockPrediction.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/stock")
public class StockPredictionController {

    @Autowired
    private RestTemplate restTemplate;

    @PostMapping("/predict")
    public ResponseEntity<String> predictStockMovement(@RequestBody Map<String, String> request) {
        // Extract the ticker from the request body
        String ticker = request.get("ticker");
        if (ticker == null || ticker.isEmpty()) {
            return ResponseEntity.badRequest().body("Ticker is missing or empty");
        }

        // Print received ticker (for debugging purposes)
        System.out.println("Received ticker: " + ticker);

        // Prepare the JSON request body for FastAPI
        Map<String, String> fastApiRequest = new HashMap<>();
        fastApiRequest.put("ticker", ticker);

        // Send the POST request to FastAPI
        String fastApiUrl = "http://localhost:8000/predict"; // Adjust the FastAPI URL if necessary
        ResponseEntity<String> fastApiResponse = restTemplate.exchange(
                fastApiUrl,
                HttpMethod.POST,
                new HttpEntity<>(fastApiRequest, new HttpHeaders()),
                String.class);

        // Return the response from FastAPI as the response from Spring Boot
        return fastApiResponse;
    }
}
