#include <stdio.h>
#include <curl/curl.h>

// Function to check if a file exists at a given URL
__declspec(dllexport) int check_file_exists(const char* url) {
    CURL* curl;
    CURLcode res;
    long response_code = 0;

    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_NOBODY, 1);
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1);
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5);

        res = curl_easy_perform(curl);
        if(res == CURLE_OK) {
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
        }
        curl_easy_cleanup(curl);
    }

    return response_code == 200;
}

int main() {
    const char* url = "http://example.com/file.txt";
    int file_exists = check_file_exists(url);

    if(file_exists) {
        printf("The file exists at the specified URL.\n");
    } else {
        printf("The file does not exist at the specified URL.\n");
    }

    return 0;
}
