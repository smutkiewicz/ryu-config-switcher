package studios.aestheticapps.ryupilot

import android.os.Bundle
import android.support.v7.app.AlertDialog
import android.support.v7.app.AppCompatActivity
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.EditText
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*
import org.apache.commons.validator.routines.InetAddressValidator

class MainActivity : AppCompatActivity()
{
    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        createIpAddressPanel()
        createSettingsPanel()
    }

    private fun createIpAddressPanel()
    {
        ipAddressTv.text = PrefsHelper.obtainRyuIpAddress(this)
        setIpAddressBtn.setOnClickListener { showIpInputDialog() }
    }

    private fun createSettingsPanel()
    {
        val settings = arrayListOf(ID_SETTING_1, ID_SETTING_2, ID_SETTING_3, ID_SETTING_4)

        setting1Btn.setOnClickListener { sendRequest(settings[0]) }
        setting2Btn.setOnClickListener { sendRequest(settings[1]) }
        setting3Btn.setOnClickListener { sendRequest(settings[2]) }
        setting4Btn.setOnClickListener { sendRequest(settings[3]) }

        setIpAddressBtn.setOnClickListener { showIpInputDialog() }
    }

    private fun showIpInputDialog()
    {
        val builder = AlertDialog.Builder(this)
        val viewInflated = LayoutInflater
            .from(this)
            .inflate(
                R.layout.ip_input_dialog,
                cardView as ViewGroup,
                false
            )

        val view = viewInflated.findViewById(R.id.inputIpTextLayout) as EditText
        view.setText(PrefsHelper.obtainRyuIpAddress(applicationContext))

        builder.apply {
            setTitle(getString(R.string.set_ryu_controller_ip))
            setView(viewInflated)
            setNegativeButton(android.R.string.cancel) { dialog, _ -> dialog.cancel() }
            setPositiveButton(android.R.string.ok) { dialog, _ -> if (checkAndSetIpAddress(view.text.toString())) dialog.dismiss() }
            show()
        }
    }

    private fun checkAndSetIpAddress(newAddress: String): Boolean
    {
        return if (InetAddressValidator.getInstance().isValid(newAddress))
        {
            PrefsHelper.setRyuIpAddress(this, newAddress)
            ipAddressTv.text = newAddress
            true
        }
        else
        {
            showToast(getString(R.string.invalid_address))
            false
        }
    }

    private fun sendRequest(settingId: Int) = RyuStringRequest(applicationContext, settingId).sendPostRequest()

    private fun showToast(text: String) = Toast.makeText(applicationContext, text, Toast.LENGTH_SHORT).show()

    private companion object
    {
        const val ID_SETTING_1 = 1
        const val ID_SETTING_2 = 2
        const val ID_SETTING_3 = 3
        const val ID_SETTING_4 = 4
    }
}
