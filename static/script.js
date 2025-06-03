document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('pitchForm');
    const generateBtn = document.getElementById('generateBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const pitchResultDiv = document.getElementById('pitchResult');
    const pitchOutputDiv = document.getElementById('pitchOutput');
    const errorResultDiv = document.getElementById('errorResult');
    const errorOutputP = document.getElementById('errorOutput');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        const merchantType = document.getElementById('merchant_type').value;
        const productInterest = document.getElementById('product_interest').value;
        const challenge = document.getElementById('challenge').value;

        // Show loading indicator and hide previous results
        loadingIndicator.style.display = 'block';
        pitchResultDiv.style.display = 'none';
        errorResultDiv.style.display = 'none';
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';


        try {
            const response = await fetch('/generate-pitch', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    merchant_type: merchantType,
                    product_interest: productInterest,
                    challenge: challenge,
                }),
            });

            loadingIndicator.style.display = 'none';
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Pitch';

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            if (data.pitch) {
                pitchOutputDiv.textContent = data.pitch;
                pitchResultDiv.style.display = 'block';
            } else if (data.error) {
                 throw new Error(data.error);
            }

        } catch (error) {
            console.error('Error:', error);
            errorOutputP.textContent = 'Failed to generate pitch: ' + error.message;
            errorResultDiv.style.display = 'block';
            loadingIndicator.style.display = 'none'; // Ensure loading is hidden on error too
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Pitch';
        }
    });
});