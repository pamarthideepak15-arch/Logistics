/* Logistics Management Platform - Universal Dropdown Handler */
document.addEventListener('DOMContentLoaded', () => {
    // Handle all details.custom-select-wrapper elements
    document.querySelectorAll('details.custom-select-wrapper').forEach(wrapper => {
        const trigger = wrapper.querySelector('summary.custom-select-trigger');
        if (!trigger) return;

        // Ensure the dropdown chevron arrow stays fixed on the far right
        const arrowSvg = trigger.querySelector('svg:last-child');
        if (arrowSvg) {
            arrowSvg.style.marginLeft = 'auto';
            arrowSvg.style.flexShrink = '0';
        }

        const placeholder = trigger.querySelector('.placeholder');
        const radios = wrapper.querySelectorAll('input[type="radio"]');

        const updateTriggerText = (radio) => {
            if (!radio) return;
            const label = radio.closest('.custom-option');
            const selectedValText = label ? label.textContent.trim() : radio.value;

            // Match specific .selected-text elements if present
            const matchedSelectedText = trigger.querySelector(`.selected-text.text-${radio.value}`);

            // Hide all .selected-text elements inside trigger
            trigger.querySelectorAll('.selected-text').forEach(el => {
                el.style.display = 'none';
            });

            if (radio.value === 'all') {
                if (placeholder) {
                    placeholder.style.display = 'flex';
                    placeholder.style.alignItems = 'center';
                    placeholder.style.gap = '6px';
                }
            } else if (matchedSelectedText) {
                if (placeholder) placeholder.style.display = 'none';
                matchedSelectedText.style.display = 'flex';
                matchedSelectedText.style.alignItems = 'center';
                matchedSelectedText.style.gap = '6px';
            } else {
                // Create dynamic selected text node if not hardcoded in markup
                let dynamicSelected = trigger.querySelector('.selected-text.dynamic-selected');
                if (!dynamicSelected) {
                    dynamicSelected = document.createElement('span');
                    dynamicSelected.className = 'selected-text dynamic-selected';
                    dynamicSelected.style.alignItems = 'center';
                    dynamicSelected.style.gap = '6px';
                    trigger.insertBefore(dynamicSelected, arrowSvg);
                }
                if (placeholder) placeholder.style.display = 'none';
                dynamicSelected.textContent = selectedValText;
                dynamicSelected.style.display = 'flex';
            }
        };

        // Initialize display text for the checked option on load
        const initialChecked = wrapper.querySelector('input[type="radio"]:checked');
        if (initialChecked) {
            updateTriggerText(initialChecked);
        }

        radios.forEach(radio => {
            radio.addEventListener('change', () => {
                updateTriggerText(radio);
                // Close dropdown unless it's a custom date trigger that opens popup
                if (radio.value !== 'customdate') {
                    wrapper.removeAttribute('open');
                }
            });
        });
    });

    // Close details dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        document.querySelectorAll('details.custom-select-wrapper[open]').forEach(wrapper => {
            if (!wrapper.contains(e.target) && !e.target.closest('.calendar-popup-overlay')) {
                wrapper.removeAttribute('open');
            }
        });
    });
});
