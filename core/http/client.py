# type: ignore
import time
import requests
from typing import Dict, Optional
from .exceptions import HTTPClientError, HTTPTimeoutError, HTTPRateLimitError, HTTPServerError, InvalidAPIKey


class HTTPClient:
    def __init__(self,
        headers: Dict[str, str],
        timeout: int = 25,
        max_retries: int = 5,
        backoff_base: int = 2
    ) -> None:
        self.headers = headers
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_base = backoff_base

    
    def _request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        files: Optional[Dict] = None,
        verify: Optional[str] = None
    ) -> Dict:

        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    headers=self.headers,
                    params=params,
                    data=data,
                    json=json,
                    files=files,
                    verify=verify,
                    timeout=self.timeout                
                )

            except requests.exceptions.Timeout:
                if attempt == self.max_retries:
                    raise HTTPTimeoutError("Request timed out")
                time.sleep((self.backoff_base ** (attempt - 1)) + 10)
                continue

            if response.status_code == 200:
                if response.headers.get("Content-Type") == "application/json":
                    if isinstance(response.json(), Dict):
                        return response.json()
                    else:
                        return {"status": "Success"}
                elif response.headers.get("Content-Type"):
                    if isinstance(response, str):
                        return response.text
                else:
                    return {"status": "Success"}
            
            if response.status_code == 204:
                if response.headers.get("Content-Type") == "application/json":
                    if isinstance(response.json(), Dict):
                        return response.json()
                    else:
                        return {"status": "Success"}
                elif response.headers.get("Content-Type"):
                    if isinstance(response, str):
                        return response.text
                else:
                    return {"status": "Success"}

            if response.status_code == 403:
                raise InvalidAPIKey()

            if response.status_code == 429:
                if attempt == self.max_retries:
                    raise HTTPRateLimitError("Rate limit exceeded")

                retry_after = response.headers.get("Retry-After")
                wait = int(retry_after) if retry_after and retry_after.isdigit() else self.backoff_base ** (attempt - 1)
                time.sleep(wait)
                continue

            if 500 <= response.status_code < 600:
                if attempt == self.max_retries:
                    raise HTTPServerError(
                        f"Server error {response.status_code}"
                    )
                time.sleep(self.backoff_base ** (attempt - 1))
                continue

            try:
                return response.json()
            except ValueError:
                return {
                    "error": {
                        "code": response.status_code,
                        "message": response.text
                    }
                }

        raise HTTPClientError("Unexpected HTTP client error")


    def get(self, url: str, params: Optional[Dict] = None, verify: Optional[str] = None) -> Dict:
        return self._request("GET", url, params=params, verify=verify)


    def post(
        self,
        url: str,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        files: Optional[Dict] = None,
        verify: Optional[str] = None
    ) -> Dict:
        return self._request("POST", url, data=data, json=json, files=files, verify=verify)


    def put(self, url: str, json: Optional[Dict] = None, verify: Optional[str] = None) -> Dict:
        return self._request("PUT", url, json=json, verify=verify)


    def delete(self, url: str, verify: Optional[str] = None) -> Dict:
        return self._request("DELETE", url, verify=verify)