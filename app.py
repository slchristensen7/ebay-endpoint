from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = "peter_piper_picked_a_peck_qje8gfx9rhn-MBM4gqt"  # paste your token here

@app.route("/ebay/deletion", methods=["GET", "POST"])
def ebay_deletion():
    # Handle eBay's challenge request
    challenge_code = request.args.get("challenge_code")
    if challenge_code:
        import hashlib
        endpoint_url = "https://your-render-url.onrender.com/ebay/deletion"
        hash_input = challenge_code + VERIFICATION_TOKEN + endpoint_url
        challenge_response = hashlib.sha256(hash_input.encode()).hexdigest()
        return jsonify({"challengeResponse": challenge_response})
    # Acknowledge deletion notifications
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run()
