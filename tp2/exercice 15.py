import json
with open("mobile_money_transactions.json", encoding="utf-8") as f:
      transactions= json.load(f)
print(f"Le nombre total de transaction est {len(transactions)}")
print(f"La première transaction est {transactions[0]}")
print(f"Les dates des transactions sont {[t['date'] for t in transactions]}")
print(f"Le solde total est {sum(t['solde'] for t in transactions)}")
transactions_recu=[t['montant'] for t in transactions if t['type'] == 'recu']
print(f"Liste comptenant uniquement les transactions reçu {transactions_recu}")
transactions_paiyer=[t['montant'] for t in transactions if t['type'] == 'paiement']
print(f"Liste comptenant uniquement les transactions payer {transactions_paiyer}")
print(f"Le montant moyen est {sum(t['montant'] for t in transactions) / len(transactions)}")
print(f"Le montant des paiements est {sum(t['montant'] for t in transactions if t['type'] == 'paiement')}")
print(f"Le montant des recu est {sum(t['montant'] for t in transactions if t['type'] == 'recu')}")
print(f"Le solde final est {sum(t['montant'] for t in transactions if t['type'] == 'recu')-sum(t['montant'] for t in transactions if t['type'] == 'paiement')}")
if sum(t['montant'] for t in transactions if t['type'] == 'recu')-sum(t['montant'] for t in transactions if t['type'] == 'paiement')==transactions[-1]['solde']:
    print("Le solde final est égal au dernier solde")
else:
    print("Le solde final est différent du dernier solde")
print(f"La  transaction avec le montant le plus élevé est {max(t['montant'] for t in transactions)}")
print(f"Les transaction avec des montant supérieur à 2000 sont : {list(t['montant'] for t in transactions if t['montant']>2000)}")

print(f"Le nombre de transaction recu est {len([t['type'] for t in transactions if t['type'] == 'recu'])}")
print(f"Le nombre de transaction payer est {len([t['type'] for t in transactions if t['type'] == 'paiement'])}")
resume = { "total_recu": sum(t['montant'] for t in transactions if t['type'] == 'recu'), "total_depense": sum(t['montant'] for t in transactions if t['type'] == 'paiement'), "solde_final": sum(t['montant'] for t in transactions if t['type'] == 'recu')-sum(t['montant'] for t in transactions if t['type'] == 'paiement'), "nombre_transactions": len(transactions), "nombre_recu": len([t['type'] for t in transactions if t['type'] == 'recu']), "nombre_paiement": len([t['type'] for t in transactions if t['type'] == 'paiement']) }
print(resume)