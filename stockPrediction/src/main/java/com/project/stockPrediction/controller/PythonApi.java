package com.project.stockPrediction.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import com.project.stockPrediction.model.StockRequest;

@RestController
public class PythonApi {

    @Autowired
    private RestTemplate restTemplate;

    @Value("${fastapi.url}")
    private String fastApiUrl;

    @PostMapping("/predict")
    public ResponseEntity<String> predictStock(@RequestBody StockRequest request) {

        Map<String, String> body = new HashMap<>();
        body.put("ticker", request.getTicker());

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<Map<String, String>> entity = new HttpEntity<>(body, headers);

        ResponseEntity<String> response = restTemplate.postForEntity(fastApiUrl, entity, String.class);

        return ResponseEntity.ok(response.getBody());
    }
}
