import React from 'react'
import { X, Copy } from 'lucide-react'

export function Modal({ isOpen, onClose, title, children, className = '', onCopy }) {
  if (!isOpen) return null

  const handleCopy = () => {
    if (onCopy) {
      onCopy()
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black/50 backdrop-blur-sm"
        onClick={onClose}
      />
      
      {/* Modal */}
      <div className={`relative bg-white rounded-xl shadow-2xl max-w-4xl w-full mx-4 max-h-[90vh] overflow-hidden ${className}`}>
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-files-light-pink bg-gradient-to-r from-files-light-gray to-files-light-pink/30">
          <h2 className="text-xl font-semibold text-files-headline-black">{title}</h2>
          <div className="flex items-center gap-2">
            {onCopy && (
              <button
                onClick={handleCopy}
                className="p-2 rounded-lg hover:bg-files-light-pink text-files-primary-red hover:text-files-maroon transition-colors"
                title="Copy content"
              >
                <Copy className="h-5 w-5" />
              </button>
            )}
            <button
              onClick={onClose}
              className="p-2 rounded-lg hover:bg-files-light-pink text-files-primary-red hover:text-files-maroon transition-colors"
            >
              <X className="h-5 w-5" />
            </button>
          </div>
        </div>
        
        {/* Content */}
        <div className="p-6 overflow-y-auto max-h-[calc(90vh-120px)]">
          {children}
        </div>
      </div>
    </div>
  )
} 