/**
 * Author: Justin Clayton
 */

'use strict';
(function() {
  $(document).ready(init);

  /** Initialize the JS to control page behavior */
  function init() {
    $('#id_password2').on('input', onCheckPW);
    $('#id_first_name, #id_last_name').on('input', onCheckName)
    $('#id_alias').on('input', onCheckAlias);
  }

  /** Validate that pws match before sending to registration. */
  function onCheckPW() {
    if ($(this).val() === $('#id_password2').val()) {
      this.setCustomValidity('');
    } else {
      this.setCustomValidity('Passwords must match.');
    }
  }

  /** Validates name fields */
  function onCheckName() {
    let re = new RegExp('^[a-zA-Z]{4,45}')
    if (re.test($(this).val())) {
      this.setCustomValidity('')
    } else {
      this.setCustomValidity('Name must be between 4 and 45 characters.')
    }
  }
})();
