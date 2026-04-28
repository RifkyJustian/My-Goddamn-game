from battery import Battery

def run_game():
    battery = Battery()
    cycle = 0

    print("🔋 EV Battery Manager Game Start")

    while True:
        cycle += 1
        print(f"\n--- Cycle {cycle} ---")
        print(battery.status())

        action = input("Choose action (charge / discharge / cool / idle): ").lower()

        if action not in ["charge", "discharge", "cool", "idle"]:
            print("Invalid action!")
            continue

        battery.apply_action(action)

        fail = battery.check_failure()
        if fail:
            print(f"\n❌ GAME OVER: {fail}")
            break

        if cycle >= 30 and battery.health > 70:
            print("\n🏆 SUCCESS: Battery managed successfully!")
            break
