import React, { useState } from 'react'
import { Copy, Check } from 'lucide-react'

export function CopyButton({ text, className = '', ...props }) {
  const [copied, setCopied] = useState(false)

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(text)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error('Failed to copy text: ', err)
      // Fallback for older browsers
      const textArea = document.createElement('textarea')
      textArea.value = text
      document.body.appendChild(textArea)
      textArea.select()
      document.execCommand('copy')
      document.body.removeChild(textArea)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    }
  }

  return (
    <button
      onClick={copyToClipboard}
      className={`inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs bg-white/90 hover:bg-white border border-files-light-pink hover:border-files-super-light-red text-files-primary-red hover:text-files-maroon rounded-lg shadow-sm hover:shadow-md transition-all duration-200 ${className}`}
      title="Copy to clipboard"
      {...props}
    >
      {copied ? (
        <>
          <Check className="h-3 w-3 text-files-primary-red" />
          Copied!
        </>
      ) : (
        <>
          <Copy className="h-3 w-3" />
          Copy
        </>
      )}
    </button>
  )
} 