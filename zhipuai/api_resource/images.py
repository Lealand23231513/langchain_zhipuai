from __future__ import annotations

from typing import Union, List, Optional, TYPE_CHECKING

import httpx

from zhipuai.core._base_api import BaseAPI
from zhipuai.core._base_type import NotGiven, NOT_GIVEN, Headers
from zhipuai.core._http_client import make_user_request_input
from zhipuai.types.image import ImagesResponded

if TYPE_CHECKING:
    from zhipuai._client import ZhipuAI


class Images(BaseAPI):
    def __init__(self, client: "ZhipuAI") -> None:
        super().__init__(client)

    def generations(
            self,
            *,
            prompt: str,
            model: str | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            quality: Optional[str] | NotGiven = NOT_GIVEN,
            response_format: Optional[str] | NotGiven = NOT_GIVEN,
            size: Optional[str] | NotGiven = NOT_GIVEN,
            style: Optional[str] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            return_json: Optional[bool] | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImagesResponded:
        _cast_type = ImagesResponded
        if return_json:
            _cast_type = object
        return self._post(
            "/images/generations",
            body={
                "prompt": prompt,
                "model": model,
                "n": n,
                "quality": quality,
                "response_format": response_format,
                "size": size,
                "style": style,
                "user": user,
            },
            options=make_user_request_input(
                extra_headers=extra_headers, timeout=timeout
            ),
            cast_type=_cast_type,
            enbale_stream=False,
        )
