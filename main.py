def hisobla_narx(masofa_km, vazn_tonna):
    narx_per_tonna_km = 500
    jami = masofa_km * vazn_tonna * narx_per_tonna_km

    chegirma_foiz = 10 if vazn_tonna > 10 else 0
    chegirma_summa = jami * chegirma_foiz / 100
    yakuniy_narx = jami - chegirma_summa

    return jami, chegirma_foiz, chegirma_summa, yakuniy_narx


def main():
    print("=== Yuk Tashish Narxini Hisoblash ===")
    masofa = float(input("Masofani kiriting (km): "))
    vazn = float(input("Yuk vaznini kiriting (tonna): "))

    jami, chegirma_foiz, chegirma_summa, yakuniy_narx = hisobla_narx(masofa, vazn)

    print(f"\nMasofa:         {masofa} km")
    print(f"Yuk vazni:      {vazn} tonna")
    print(f"Asosiy narx:    {jami:,.0f} so'm")

    if chegirma_foiz > 0:
        print(f"Chegirma:       -{chegirma_foiz}% (-{chegirma_summa:,.0f} so'm)")

    print(f"Jami narx:      {yakuniy_narx:,.0f} so'm")


if __name__ == "__main__":
    main()
