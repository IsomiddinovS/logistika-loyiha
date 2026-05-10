def hisobla_narx(masofa_km, vazn_tonna):
    narx_per_tonna_km = 500
    return masofa_km * vazn_tonna * narx_per_tonna_km


def main():
    print("=== Yuk Tashish Narxini Hisoblash ===")
    masofa = float(input("Masofani kiriting (km): "))
    vazn = float(input("Yuk vaznini kiriting (tonna): "))

    narx = hisobla_narx(masofa, vazn)

    print(f"\nMatsofa:    {masofa} km")
    print(f"Yuk vazni:  {vazn} tonna")
    print(f"Jami narx:  {narx:,.0f} so'm")


if __name__ == "__main__":
    main()
