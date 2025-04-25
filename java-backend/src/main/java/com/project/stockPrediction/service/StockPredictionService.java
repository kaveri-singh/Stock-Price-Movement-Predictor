package com.project.stockPrediction.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.project.stockPrediction.model.PredictionResponse;

@Service
public class StockPredictionService {

    private final String ML_API_URL = "http://localhost:8000/predict"; // URL of the Python ML API

    public PredictionResponse getPrediction(String ticker) {
        RestTemplate restTemplate = new RestTemplate();
        String url = ML_API_URL + "?ticker=" + ticker;
        return restTemplate.getForObject(url, PredictionResponse.class);
    }
}
