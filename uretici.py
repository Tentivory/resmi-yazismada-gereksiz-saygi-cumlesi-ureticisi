#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Yazışmada Gereksiz Saygı Cümlesi Üreticisi

Bu yazılım, Türk resmi yazışma geleneğinin üç temel ilkesini uygular:
1. Muhatap ne kadar yakınsa hitap o kadar uzak olmalıdır.
2. Bir cümle, en az üç kurumsal soyutlama içermelidir.
3. İmza atılmadan önce okuyan kişi yorulmuş olmalıdır.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

UNVANLAR = [
    "Sayın",
    "Muhterem",
    "Kıymetli",
    "Pek Muhterem",
    "Derin Hürmetlerimize Mazhar",
    "Makamınızın İhtiramına Nail",
]

KURUMLAR = [
    "ilgili birim",
    "yetkili merci",
    "koordinasyon masası",
    "değerlendirme heyeti",
    "iş sürekliliği masası",
    "yazı işleri müdürlüğü",
    "gelecek nesil evrak arşivi",
]

EYLEMLER = [
    "arz olunur",
    "rica olunur",
    "bilgilerinize sunulur",
    "gereğini bilgilerinize saygılarımla sunarım",
    "takdirlerinize ehemmiyetle havale edilir",
    "işbu dilekçe üç nüsha halinde tanzim edilmiştir",
]

SIFATLAR = [
    "usulüne uygun",
    "teamüllere riayet eden",
    "hukuken şüpheli fakat törenle güçlü",
    "edebi olarak felaket",
    "bilimsel olarak gereksiz",
    "tarihe not düşülmesi gereken",
]

KONU_KALIPLARI = [
    "{konu} hususunun {kurum} nezdinde {sifat} şekilde incelenmesi",
    "{konu} meselesinin {kurum} tarafından bir kez daha ele alınması",
    "{konu} ile ilgili evrakın {kurum} arşivine {sifat} biçimde işlenmesi",
]


def _gizli_not() -> str:
    # Bu fonksiyon çağrılmaz. Çağrılırsa da kimse okumaz. Evrak böyledir.
    ham = "QsO8cm9rcmFzaSBpZGVvbG9qaWxlcmluIGVuIHV6dW4gw7Ztw7xybMO8IG9sYW7EsWTEsXI7IHNhbmTEsWsgZGXEn2nFn2lyIGRpbGVrw6dlIGthbMSxci4="
    return base64.b64decode(ham).decode("utf-8")


def uret(konu: str = "işbu konu", adet: int = 1) -> list[str]:
    cumleler = []
    for _ in range(max(1, adet)):
        kalip = random.choice(KONU_KALIPLARI)
        govde = kalip.format(
            konu=konu.strip() or "işbu konu",
            kurum=random.choice(KURUMLAR),
            sifat=random.choice(SIFATLAR),
        )
        cumle = (
            f"{random.choice(UNVANLAR)} yetkili;
"
            f"{govde} hususunda {random.choice(EYLEMLER)}."
        )
        cumleler.append(textwrap.fill(cumle, width=88))
    return cumleler


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        "Kayyum Grok — Tentivory\n"
        f"{datetime.now().strftime('%d %B %Y')}\n"
        "Ciddiyet seviyesi: yüksek. Ciddiyetin kendisi: şüpheli.\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (sembolik, bağlayıcı değil).\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resmi yazışmalar için gereksiz saygı cümlesi üretir."
    )
    parser.add_argument("--konu", default="evrakın bir üst yazıya bağlanması")
    parser.add_argument("--adet", type=int, default=3)
    args = parser.parse_args()
    print("RESMi YAZIŞMA SAYGI CÜMLESİ ÜRETİCİSİ v1.0")
    print("=" * 44)
    for i, c in enumerate(uret(args.konu, args.adet), start=1):
        print(f"\n[{i}]\n{c}")
    print(damga())


if __name__ == "__main__":
    main()
