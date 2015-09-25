#include "HttpClient/HttpClient.h"
#include <string.h>

HttpClient http;

http_header_t headers[] = {
      { "Content-Type", "application/x-www-form-urlencoded" },
      { NULL, NULL } // NOTE: Always terminate headers will NULL
};

http_request_t request;
http_response_t response;

void setup() {
    request.hostname = "devops-day.cfapps.io";
    request.port = 80;
    request.path = "/collect";
    Serial.begin(9600);
}

void loop() {
    int analogValue = analogRead(A0);
    double voltage = 3.3 * ((double)analogValue / 4095.0);
    int temperature = (voltage - 0.5) * 100;
    
    request.body = "temp=" + String(temperature);
    http.post(request, response, headers);
    
    Serial.println(response.body);
    
    delay(2000);
}
