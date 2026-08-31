# -*- coding: utf-8 -*-
import io

add_path = u"c:/Users/DK/Desktop/Logistics/Staff-Management/add-employee.html"
edit_path = u"c:/Users/DK/Desktop/Logistics/Staff-Management/edit-employee.html"

def replace_in_file(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize CRLF to LF
    original_crlf = '\r\n' in content
    content = content.replace('\r\n', '\n')

    for find_text, replace_text in replacements:
        find_norm = find_text.replace('\r\n', '\n')
        replace_norm = replace_text.replace('\r\n', '\n')
        
        if find_norm in content:
            content = content.replace(find_norm, replace_norm)
            print(u"Successfully replaced in {}".format(path))
        else:
            print(u"WARNING: Match not found in {}".format(path))

    # Restore CRLF if present originally
    if original_crlf:
        content = content.replace('\n', '\r\n')

    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(content)

add_replacements = [
    (
        u'''                                            <select id="ot-rate" name="ot-rate" style="width:100%;" onchange="onOtRateChange(); calcSalary();">
                                                <option value="">— Select OT Rate —</option>
                                                <option value="1">1× (Regular)</option>
                                                <option value="1.5">1.5× (Standard OT)</option>
                                                <option value="2">2× (Double Time)</option>
                                                <option value="custom">Custom</option>
                                            </select>''',
        u'''                                            <input type="hidden" id="ot-rate" name="ot-rate" value="">
                                            <details class="custom-select-wrapper" id="ot-rate-wrapper">
                                                <summary class="custom-select-trigger">
                                                    <span class="placeholder">— Select OT Rate —</span>
                                                    <span class="selected-text text-1">1× (Regular)</span>
                                                    <span class="selected-text text-1_5">1.5× (Standard OT)</span>
                                                    <span class="selected-text text-2">2× (Double Time)</span>
                                                    <span class="selected-text text-custom">Custom</span>
                                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="12" height="12"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                                </summary>
                                                <div class="custom-select-options">
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="1" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> 1× (Regular)</label>
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="1.5" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> 1.5× (Standard OT)</label>
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="2" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> 2× (Double Time)</label>
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="custom" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> Custom</label>
                                                </div>
                                            </details>'''
    ),
    (
        u'''                                            <select id="increment-type" name="increment-type" style="width:100%;" onchange="onIncrTypeChange(); calcSalary();">
                                                <option value="">— Select Type —</option>
                                                <option value="pct">Percentage (%)</option>
                                                <option value="amt">Fixed Amount (₹)</option>
                                            </select>''',
        u'''                                            <input type="hidden" id="increment-type" name="increment-type" value="">
                                            <details class="custom-select-wrapper" id="increment-type-wrapper">
                                                <summary class="custom-select-trigger">
                                                    <span class="placeholder">— Select Type —</span>
                                                    <span class="selected-text text-pct">Percentage (%)</span>
                                                    <span class="selected-text text-amt">Fixed Amount (₹)</span>
                                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="12" height="12"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                                </summary>
                                                <div class="custom-select-options">
                                                    <label class="custom-option"><input type="radio" name="increment-type-radio" value="pct" onchange="document.getElementById('increment-type').value = this.value; onIncrTypeChange(); calcSalary();"> Percentage (%)</label>
                                                    <label class="custom-option"><input type="radio" name="increment-type-radio" value="amt" onchange="document.getElementById('increment-type').value = this.value; onIncrTypeChange(); calcSalary();"> Fixed Amount (₹)</label>
                                                </div>
                                            </details>'''
    )
]

edit_replacements = [
    (
        u'''                                            <select id="ot-rate" name="ot-rate" style="width:100%;" onchange="onOtRateChange(); calcSalary();">
                                                <option value="">— Select OT Rate —</option>
                                                <option value="1">1× (Regular)</option>
                                                <option value="1.5" selected>1.5× (Standard OT)</option>
                                                <option value="2">2× (Double Time)</option>
                                                <option value="custom">Custom</option>
                                            </select>''',
        u'''                                            <input type="hidden" id="ot-rate" name="ot-rate" value="1.5">
                                            <details class="custom-select-wrapper" id="ot-rate-wrapper">
                                                <summary class="custom-select-trigger">
                                                    <span class="placeholder">— Select OT Rate —</span>
                                                    <span class="selected-text text-1">1× (Regular)</span>
                                                    <span class="selected-text text-1_5">1.5× (Standard OT)</span>
                                                    <span class="selected-text text-2">2× (Double Time)</span>
                                                    <span class="selected-text text-custom">Custom</span>
                                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="12" height="12"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                                </summary>
                                                <div class="custom-select-options">
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="1" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> 1× (Regular)</label>
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="1.5" checked onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> 1.5× (Standard OT)</label>
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="2" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> 2× (Double Time)</label>
                                                    <label class="custom-option"><input type="radio" name="ot-rate-radio" value="custom" onchange="document.getElementById('ot-rate').value = this.value; onOtRateChange(); calcSalary();"> Custom</label>
                                                </div>
                                            </details>'''
    ),
    (
        u'''                                            <select id="increment-type" name="increment-type" style="width:100%;" onchange="onIncrTypeChange(); calcSalary();">
                                                <option value="">— Select Type —</option>
                                                <option value="pct">Percentage (%)</option>
                                                <option value="amt">Fixed Amount (₹)</option>
                                            </select>''',
        u'''                                            <input type="hidden" id="increment-type" name="increment-type" value="">
                                            <details class="custom-select-wrapper" id="increment-type-wrapper">
                                                <summary class="custom-select-trigger">
                                                    <span class="placeholder">— Select Type —</span>
                                                    <span class="selected-text text-pct">Percentage (%)</span>
                                                    <span class="selected-text text-amt">Fixed Amount (₹)</span>
                                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="12" height="12"><polyline points="6 9 12 15 18 9"></polyline></svg>
                                                </summary>
                                                <div class="custom-select-options">
                                                    <label class="custom-option"><input type="radio" name="increment-type-radio" value="pct" onchange="document.getElementById('increment-type').value = this.value; onIncrTypeChange(); calcSalary();"> Percentage (%)</label>
                                                    <label class="custom-option"><input type="radio" name="increment-type-radio" value="amt" onchange="document.getElementById('increment-type').value = this.value; onIncrTypeChange(); calcSalary();"> Fixed Amount (₹)</label>
                                                </div>
                                            </details>'''
    )
]

replace_in_file(add_path, add_replacements)
replace_in_file(edit_path, edit_replacements)
print("Replacement complete.")
