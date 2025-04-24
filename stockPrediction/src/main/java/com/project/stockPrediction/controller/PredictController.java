package com.project.stockPrediction.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.project.stockPrediction.model.StockRequest;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/stock")
public class PredictController {

    @PostMapping("/predict")
    public ResponseEntity<?> getDetails(@RequestBody StockRequest request) {
        return new ResponseEntity<>(request, HttpStatus.OK);
    }

}
