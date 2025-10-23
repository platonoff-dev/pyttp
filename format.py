from typing import Self


class Request:
    def __init__(
            self,
            method: str,
            path: str,
            protocol: str,
            headers: dict[str, str],
            body: bytes | None,
    ) -> None:
        self.method = method
        self.path = path
        self.protocol = protocol
        self.headers = headers
        self.body = body
        
    @classmethod
    def parse(cls, data: bytes) -> Self:
        lines = data.split(b"\r\n")
        top_line_parts = lines[0].split(b" ")
        method = top_line_parts[0]
        path = top_line_parts[1]
        protocol = top_line_parts[2]

        headers = {}

        i = 1
        while i < len(lines) and lines[i] != b"":
            k, v = lines[i].split(b": ")
            headers[k.decode()] = v.decode()
            i += 1

        body = None
        if i < len(lines) - 1:
            body = b"\n".join(lines[i+1:])

        return cls(
            method=method.decode(),
            path=path.decode(),
            protocol=protocol.decode(),
            headers=headers,
            body=body,
        )
    

class Response:
    def __init__(
        self,
        protocol: str,
        code: int,
        status: str,
        headers: dict[str, str],
        body: bytes,
    ) -> None:
        pass

    def encode(self) -> bytes:
        return "".encode()