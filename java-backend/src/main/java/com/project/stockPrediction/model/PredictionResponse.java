package com.project.stockPrediction.model;

public class PredictionResponse {
    private String prediction;
    private double confidence;

    // Getters and Setters
    public String getPrediction() {
        return prediction;
    }

    public void setPrediction(String prediction) {
        this.prediction = prediction;
    }

    public double getConfidence() {
        return confidence;
    }

    public void setConfidence(double confidence) {
        this.confidence = confidence;
    }
}
